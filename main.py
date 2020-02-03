from src.atlas import Atlas

if __name__ == "__main__":
    atlas = Atlas()
    atlas.create_project(
        "AtlasTest", "/", "users", "spencerpost", "Source", "my_project_bootstrapper"
    )
    atlas.bootstrap("AtlasTest")
