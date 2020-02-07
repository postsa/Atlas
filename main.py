from src.atlas import Atlas
from src.db.db_factory import DbFactory
from sys import argv


if __name__ == "__main__":
    db = DbFactory().get_db(
        "file_system",
        "/",
        "users",
        "spencerpost",
        "Source",
        "the_atlas_demo",
        "storage",
    )
    atlas = Atlas(db)
    # atlas.create_project(
    #     "AtlasDemo",
    #     argv[1],
    #     "theatlasdemo.com",
    #     "/",
    #     "users",
    #     "spencerpost",
    #     "Source",
    #     "the_atlas_demo",
    #     "project",
    #     "bootstrapper",
    # )
    # atlas.bootstrap("AtlasDemo")
    # atlas.add_service(
    #     "AtlasDemo",
    #     "nginx1",
    #     "/",
    #     "users",
    #     "spencerpost",
    #     "Source",
    #     "the_atlas_demo",
    #     "project",
    #     "nginx1",
    # )
    atlas.add_service(
        "AtlasDemo",
        "subproject",
        "/",
        "users",
        "spencerpost",
        "Source",
        "the_atlas_demo",
        "project",
        "subproject",
    )
