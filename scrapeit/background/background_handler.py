
class BackgroundHandler(object):
    def __init__(self, storage_path : str) -> None:
        self.storage_path = storage_path

    def change_background(file_path: str) -> None:
        raise NotImplementedError("Can't change background")