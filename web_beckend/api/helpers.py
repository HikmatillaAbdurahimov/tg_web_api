import uuid


class SaveMediaFiles(object):
    def save_artist_image(instanse, filename):
        image_path=filename.split('.')[-1]
        return f"artist/{uuid.uuid4()}.{image_path}"

    def save_albom_image(instanse, filename):
        image_path = filename.split('.')[-1]
        return f"albom/{uuid.uuid4()}.{image_path}"

    def save_songs_image(instanse, filename):
        image_path = filename.split('.')[-1]
        return f"song/{uuid.uuid4()}.{image_path}"
