from bears.xml2.XCopBear import XCopBear
from coalib.testing.LocalBearTestHelper import verify_local_bear

valid_file = """
<?xml version="1.0"?>
<test>
Hello, world
</test>
"""

invalid_file="""
<test>
open
</tes>
"""

HTMLLintBearTest = verify_local_bear(XCopBear,
                                     valid_files=(valid_file),
                                     invalid_files=(invalid_file,),
                                     tempfile_kwargs={'suffix': '.xml'})
