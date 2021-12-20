from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram('', __file__[:-3], show=False):
    ELB('elb') >> EC2('web') >> RDS('userdb')