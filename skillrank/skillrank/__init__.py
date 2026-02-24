import pymysql

# Make PyMySQL present itself as a recent mysqlclient to satisfy Django's
# version check (Django requires mysqlclient >= 2.2.1). PyMySQL's bundled
# compatibility info reports 1.4.6 which triggers Django's error, so override
# the values before installing the MySQLdb shim.
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.__version__ = "2.2.1"

# Use PyMySQL as MySQLdb replacement so Django's MySQL backend works
pymysql.install_as_MySQLdb()

