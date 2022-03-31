from collections import defaultdict

from fileseq import FrameSet
from sqlalchemy import func

from zou.app import db
from zou.app.models.entity import Entity
from zou.app.models.project import Project
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
    existing_validation = shots_service.get_shot_raw(shot_id).validation_history
    input_frame_set = FrameSet(data["frame_set"])
    frame_set = FrameSet(input_frame_set)

    if existing_validation:
        existing_frame_set = FrameSet(existing_validation[-1].frame_set)
        combined_frameset = list(input_frame_set) + list(existing_frame_set)
        if substract:
            combined_frameset = [frame for frame in existing_frame_set if frame not in input_frame_set]
        combined_frameset.sort()
        frame_set = FrameSet(combined_frameset)

    validation_record = ValidationRecord.create(
        shot_id=shot_id,
        frame_set=str(frame_set),
        total=len(frame_set)
    )

    return validation_record.serialize()


def get_project_progress(project_id):
    truncated_date = func.date_trunc("day", ValidationRecord.created_at)
    progress_query = (
        db.session.query(truncated_date, ValidationRecord.total, ValidationRecord.shot_id)
        .distinct(truncated_date, ValidationRecord.shot_id)
        .filter(ValidationRecord.shot_id==Entity.id)
        .filter(Entity.project_id==project_id)
        .order_by(truncated_date, ValidationRecord.shot_id, ValidationRecord.created_at.desc())
    )
    progress_data = progress_query.all()

    project_progress = defaultdict(lambda: {"total": 0, "shots": []})
    for date, total, shot in progress_data[::-1]:
        if shot in project_progress[date]["shots"]:
            continue
        project_progress[date]["total"] += total
        project_progress[date]["shots"].append(shot)

    return [{"date": key, "total": value["total"]} for key, value in project_progress.items()]
