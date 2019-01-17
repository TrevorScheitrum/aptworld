from package_parser import PackageParser

# create instance of FileParser Class so that we can parse a normal text file, and a gunzipped file
PackageParser = PackageParser()

# Parse the dpkg/status file to get a list of currently installed packages
dpkg_packages = PackageParser.parse_file('/var/lib/dpkg/status')

# Parse the initial-status.gz so that we can compare what's included with a new system, vs what's installed currently
initial_packages = PackageParser.parse_file('/var/log/installer/initial-status.gz')

# Throw the dictionaries for dpkg/status and initial-status.gz into sets so we can get the difference of packages.
# This will give us only packages that have been manually installed after the system was installed.
user_packages = set(dpkg_packages)-set(initial_packages)
user_packages = sorted(user_packages)

for package in user_packages:
    print(package)