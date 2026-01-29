import eoupv2

def test_package_imports():
    assert eoupv2 is not None

def test_load_sample_data():
    data = eoupv2.load_sample_netcdf()
    assert data is not None