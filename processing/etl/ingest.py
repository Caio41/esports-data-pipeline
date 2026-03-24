import os
import sys

import gdown
from datetime import datetime 


def download_data(output_path: str):
    
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    file_id = '1hnpbrUpBMS1TZI7IovfpKeZfWJH1Aptm' # oracle elixir matches google drive folder
    
    gdown.download(id=file_id, output=output_path)
    print(output_path)


if __name__ == '__main__':
    output_path = sys.argv[1]
    download_data(output_path)