from .db_instance import db


class Selection(db.Model):
    __tablename__ = 'selections'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    submit_time = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    first_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    second_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    third_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    final_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    first_topic = db.relationship('Topic', foreign_keys=[first_topic_id])
    second_topic = db.relationship('Topic', foreign_keys=[second_topic_id])
    third_topic = db.relationship('Topic', foreign_keys=[third_topic_id])
    final_topic = db.relationship('Topic', foreign_keys=[final_topic_id])

    def __init__(self, student_id):
        self.student_id = student_id
        self.status = 0

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, student_id, submit_time, status, first_topic_id, second_topic_id, third_topic_id, final_topic_id):
        self.student_id = student_id
        self.submit_time = submit_time
        self.status = status
        self.first_topic_id = first_topic_id
        self.second_topic_id = second_topic_id
        self.third_topic_id = third_topic_id
        self.final_topic_id = final_topic_id
        db.session.commit()

    @property
    def first_topic_name(self):
        return self.first_topic.name

    @property
    def second_topic_name(self):
        return self.second_topic.name

    @property
    def third_topic_name(self):
        return self.third_topic.name

    @property
    def final_topic_name(self):
        return self.final_topic.name

    @classmethod
    def get_by_student_id(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first()

    def __repr__(self):
        return f'<Selection {self.id}>'
