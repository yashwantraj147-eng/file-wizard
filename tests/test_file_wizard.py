import wizard
from wizard.readers import BaseReader
from wizard.writers import BaseWriter


def test_wizard_version():
    """Verify that wizard version metadata is defined."""
    assert wizard.__version__ == "0.1.0"


def test_base_interfaces():
    """Verify BaseReader and BaseWriter ABC interfaces."""
    assert issubclass(BaseReader, object)
    assert issubclass(BaseWriter, object)
