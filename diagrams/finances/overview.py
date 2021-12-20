from diagrams import Diagram
from diagrams.programming.language import Python
from diagrams.generic.storage import Storage as StorageLocal
from diagrams.gcp.storage import Storage as StorageGCP

with Diagram('', str(__file__).replace('.py',''), show=False):

    local = StorageLocal('Local')
    
    Python('Scrawler Itaú') >> local
    Python('Scrawler NuBank') >> local

    local << Python('upsert') >> StorageGCP('Spreadsheet')
    