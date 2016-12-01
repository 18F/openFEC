from .base import db
from sqlalchemy.dialects.postgresql import TSVECTOR

from webservices import docs


class RadAnalyst(db.Model):
    __tablename__ = 'ofec_rad_mv'

    idx = db.Column(db.Integer, primary_key=True)
    committee_id = db.Column(db.String, primary_key=True, index=True, doc=docs.COMMITTEE_ID)
    committee_name = db.Column(db.String(100), index=True, doc=docs.COMMITTEE_NAME)
    analyst_id = db.Column(db.Numeric(38, 0), index=True, doc='ID of RAD analyst.')
    analyst_short_id = db.Column(db.Numeric(4, 0), doc='Short ID of RAD analyst.')
    first_name = db.Column(db.String(255), index=True, doc='Fist name of RAD analyst')
    last_name = db.Column(db.String(100), index=True, doc='Last name of RAD analyst')
    telephone_ext = db.Column(db.Numeric(4, 0), index=True, doc='Telephone extension of RAD analyst')
    rad_branch = db.Column(db.String(100), index=True, doc='Branch of RAD analyst')
    name_txt = db.Column(TSVECTOR)
