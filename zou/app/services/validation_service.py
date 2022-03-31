from collections import defaultdict
from typing import cast

from fileseq import FrameSet
from sqlalchemy import func

from zou.app import db
from zou.app.models.entity import Entity
from zou.app.models.validation_record import ValidationRecord
from zou.app.services import (
    shots_service,
)


def get_validation_record(validation_id):
    """
    Return the progress as an active record.
    """
    validation_record = ValidationRecord.get_by(id=validation_id)
    return validation_record.serialize()


def create_validation_record(shot_id, data={}, substract=False):
    """
    Create progress record for given shot.
    """
    shot = shots_service.get_shot_raw(shot_id)
    existing_validation = shot.validation_history
    input_frame_set = FrameSet(data["frame_set"])
    frame_set = FrameSet(input_frame_set)

    # Patch the current latest validation frame set
    if existing_validation:
        existing_frame_set = FrameSet(existing_validation[-1].frame_set)
        if substract:
            frame_set = existing_frame_set.difference(frame_set)
        else:
            frame_set = existing_frame_set.union(frame_set)

    # Make sure the new frame set does not exeed the amount of frames
    frame_set = FrameSet.from_iterable(
        [frame for frame in frame_set.items if frame <= shot.nb_frames]
    )

    validation_record = ValidationRecord.create(
        shot_id=shot_id, frame_set=str(frame_set), total=len(frame_set)
    )

    return validation_record.serialize()


def get_project_progress(project_id):
    truncated_date = func.date_trunc("day", ValidationRecord.created_at)
    progress_query = (
        db.session.query(
            truncated_date,
            ValidationRecord.total,
            ValidationRecord.shot_id,
            Entity.nb_frames,
        )
        .distinct(truncated_date, ValidationRecord.shot_id)
        .filter(ValidationRecord.shot_id == Entity.id)
        .filter(Entity.project_id == project_id)
        .order_by(
            truncated_date,
            ValidationRecord.shot_id,
            ValidationRecord.created_at.desc(),
        )
    )
    progress_data = progress_query.all()

    project_progress = defaultdict(
        lambda: {"total": 0, "shots": [], "progress": 0}
    )
    for date, total, shot, nb_frames in progress_data[::-1]:
        if shot in project_progress[date]["shots"] and nb_frames is not 0:
            continue

        shots = cast(list, project_progress[date]["shots"])
        progress = cast(int, project_progress[date]["progress"])
        progress = progress * (len(shots) / (len(shots) + 1)) + (
            (total / nb_frames) / (len(shots) + 1)
        )

        project_progress[date]["progress"] = progress
        project_progress[date]["total"] += total
        shots.append(shot)

    progress = [
        {"date": key, "total": value["total"], "progress": value["progress"]}
        for key, value in project_progress.items()
    ]
    progress.sort(key=lambda x: x["date"])
    return progress
