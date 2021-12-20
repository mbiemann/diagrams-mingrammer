from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram('', __file__[:-3], show=False):
    EC2('server')