from abc import ABC
import os


class Writer(ABC):
    """Write STCZYX data arrays to file, with accompanying metadata
    Will overwrite existing files of same name.

    Example:
        1) construct and use as object
        image = numpy.ndarray([1, 10, 3, 1024, 2048])
        writer = DerivedWriter("file.ome.tif")
        writer.save(image)
        writer.close()

        2) use the "with" pattern
        image2 = numpy.ndarray([5, 486, 210])
        # There needs to be some sort of data inside the image2 array
        with DerivedWriter("file2.ome.tif") as writer2:
            write2.set_metadata(myMetaData)
            writer2.save(image2)
    """

    def __init__(self, file_path):
        """
        Class initializer
        :param file_path: path to image output location
        """
        self.file_path = file_path
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    @abstractmethod
    def close(self):
        """Close file and del objects"""
        pass

    @abstractmethod
    def save(self, data, dims="STCZYX", **kwargs):  # Dave altered from dims=None):
        """Write to open file"""
        pass
