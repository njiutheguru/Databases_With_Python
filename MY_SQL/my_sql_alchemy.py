from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from sqlalchemy.orm import registry


password = input("Enter you MYSQL password:")

engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/Projects',echo=True)

mapper_registry = registry()
#mapper_registry.metadata

base = mapper_registry.generate_base()

class Project(base):
    __tablename__ = 'Projects'
    project_id = Column(Integer, primary_key = True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project (title={0}, description={1})>".format(self.title, self.description)
    

class Task(base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))
    
    project = relationship("Project")


    def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)
    

base.metadata.create_all(engine)










