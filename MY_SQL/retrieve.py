from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import relationship, Session
from sqlalchemy import ForeignKey, select

from sqlalchemy.orm import registry


password = input("Enter you MYSQL password:")

engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/Projects',echo=True)

mapper_registry = registry()
#mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'Projects'
    project_id = Column(Integer, primary_key = True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project (title={0}, description={1})>".format(self.title, self.description)
    

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))
    
    project = relationship("Project")


    def __repr__(self):
        return "<Task(description='{0}')>".format(self.description)
    

Base.metadata.create_all(engine)

with Session(engine) as session:
    smt =select(Project).where(Project.title =='Organize closet')
    results = session.execute(smt)
    organize_closet_project = results.scalar()

    smt = select(Task).where(Task.project_id == organize_closet_project.project_id)
    results = session.execute(smt)
    for task in results:
        print(task)

