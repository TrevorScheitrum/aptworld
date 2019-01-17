import gzip

class PackageParser:

    # function to parse a generic file, determines file type based on extension
    def parse_file(self,file):
        if file[-2:] == "gz":
            return self.parse_gz_file(file)
        else:
            return self.parse_text_file(file)
    
    # opens a text file to read the contents, so we can parse out the package names
    def parse_text_file(self,file):
        file_contents = ""
        try:
            with open(file, 'r') as f:
                file_contents = f.readlines()
            f.closed
        except IOError:
            print(f'An error occured trying to read the file: {file}')
            raise SystemExit(0)
           
        packages = self.parse_packages(file_contents)
        return packages

    # opens a gunzipped text file to read the contents, so we can parse out the package names
    # has to be opened with gzip.open() intead of or normal open() command
    def parse_gz_file(self,file):
        file_contents = ""
        try:
            with gzip.open(file, 'rt') as f:
                file_contents = f.readlines()
            f.closed
        except IOError:
            print(f'An error occured trying to read the file: {file}')
            raise SystemExit(0)       

        packages = self.parse_packages(file_contents)
        return packages

    # Parse out the package names from the file contents
    def parse_packages(self, file_contents):
        packages = {}
        for line in file_contents:
            index = line.find("Package: ")
            # remove the "Package: " text of each line so we can isolate just the package names
            if index >= 0:
                package = line[index+9:-1]
                packages[package] = package
        return packages