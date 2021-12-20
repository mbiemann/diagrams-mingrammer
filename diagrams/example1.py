from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram('', str(__file__).replace('.py',''), show=False):
    EC2('server')