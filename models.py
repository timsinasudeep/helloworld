from typing import List


from db import db


class TaskModel(db.Model):
    __tablename__="tasks"
    
    id =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False,unique=True)
    done=db.Column(db.Boolean,default=False)

    @classmethod
    def find_by_id(cls, id: int) -> "TaskModel":
        return cls.query.filter_by(id=id).first()
    @classmethod
    def find_all(cls) -> List["TaskModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()