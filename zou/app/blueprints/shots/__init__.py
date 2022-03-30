from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from .resources import (
    ShotResource,
    ShotsResource,
    AllShotsResource,
    ShotsAndTasksResource,
    ShotAssetsResource,
    ShotPreviewsResource,
    ShotValidationResource,
    ShotTaskTypesResource,
    ShotTasksResource,
    ShotVersionsResource,
    SceneResource,
    ScenesResource,
    SceneAndTasksResource,
    SceneTasksResource,
    SceneTaskTypesResource,
    SceneShotsResource,
    RemoveShotFromSceneResource,
    ProjectShotsResource,
    ProjectScenesResource,
    ProjectSequencesResource,
    ProjectEpisodesResource,
    ProjectEpisodeStatsResource,
    ProjectEpisodeRetakeStatsResource,
    EpisodeResource,
    EpisodesResource,
    EpisodeShotsResource,
    EpisodeAndTasksResource,
    EpisodeSequencesResource,
    EpisodeTasksResource,
    EpisodeTaskTypesResource,
    SequenceResource,
    SequencesResource,
    SequenceShotsResource,
    SequenceAndTasksResource,
    SequenceScenesResource,
    SequenceTasksResource,
    SequenceTaskTypesResource,
    EpisodeShotTasksResource,
    SequenceShotTasksResource,
)

routes = [
    ("/data/shots", AllShotsResource),
    ("/data/shots/all", ShotsResource),
    ("/data/shots/with-tasks", ShotsAndTasksResource),
    ("/data/shots/<shot_id>", ShotResource),
    ("/data/shots/<shot_id>/assets", ShotAssetsResource),
    ("/data/shots/<shot_id>/task-types", ShotTaskTypesResource),
    ("/data/shots/<shot_id>/tasks", ShotTasksResource),
    ("/data/shots/<shot_id>/preview-files", ShotPreviewsResource),
    ("/data/shots/<shot_id>/versions", ShotVersionsResource),
    ("/data/shots/<shot_id>/validation", ShotValidationResource),
    ("/data/scenes/all", ScenesResource),
    ("/data/scenes/with-tasks", SceneAndTasksResource),
    ("/data/scenes/<scene_id>", SceneResource),
    ("/data/scenes/<scene_id>/tasks", SceneTasksResource),
    ("/data/scenes/<scene_id>/task-types", SceneTaskTypesResource),
    ("/data/scenes/<scene_id>/shots", SceneShotsResource),
    ("/data/scenes/<scene_id>/shots/<shot_id>", RemoveShotFromSceneResource),
    ("/data/episodes", EpisodesResource),
    ("/data/episodes/with-tasks", EpisodeAndTasksResource),
    ("/data/episodes/<episode_id>", EpisodeResource),
    ("/data/episodes/<episode_id>/shots", EpisodeShotsResource),
    ("/data/episodes/<episode_id>/sequences", EpisodeSequencesResource),
    ("/data/episodes/<episode_id>/tasks", EpisodeTasksResource),
    ("/data/episodes/<episode_id>/task-types", EpisodeTaskTypesResource),
    ("/data/episodes/<episode_id>/shot-tasks", EpisodeShotTasksResource),
    ("/data/sequences", SequencesResource),
    ("/data/sequences/with-tasks", SequenceAndTasksResource),
    ("/data/sequences/<sequence_id>", SequenceResource),
    ("/data/sequences/<sequence_id>/shots", SequenceShotsResource),
    ("/data/sequences/<sequence_id>/scenes", SequenceScenesResource),
    ("/data/sequences/<sequence_id>/tasks", SequenceTasksResource),
    ("/data/sequences/<sequence_id>/task-types", SequenceTaskTypesResource),
    ("/data/sequences/<sequence_id>/shot-tasks", SequenceShotTasksResource),
    ("/data/projects/<project_id>/shots", ProjectShotsResource),
    ("/data/projects/<project_id>/scenes", ProjectScenesResource),
    ("/data/projects/<project_id>/sequences", ProjectSequencesResource),
    ("/data/projects/<project_id>/episodes", ProjectEpisodesResource),
    (
        "/data/projects/<project_id>/episodes/stats",
        ProjectEpisodeStatsResource,
    ),
    (
        "/data/projects/<project_id>/episodes/retake-stats",
        ProjectEpisodeRetakeStatsResource,
    ),
]


blueprint = Blueprint("shots", "shots")
api = configure_api_from_blueprint(blueprint, routes)
