"""API endpoints."""
from britecoreproject import app, dbfunctions, orm, sample_data
import json

@app.route('/hello')
def hello():
    """Hello World."""
    return 'Hello world!'

@app.route('/initdb')
def init_db():
    """Set up the database."""
    db = dbfunctions.init_db()
    sample_data.insert_sample_data()
    return 'Database is good to go!'

@app.route('/risk/<int:id>')
def risk_by_id(id):
    """Get a risk, given its ID."""
    db = dbfunctions.get_db()
    risk = orm.RiskType.get(id)
    risk_dict = make_risk_dict(risk)
    return json.dumps(risk_dict, indent=2)

@app.route('/allrisks')
def all_risks():
    """Get all risks."""
    db = dbfunctions.get_db()
    risks = orm.RiskType.select()
    risk_list = []
    for risk in risks:
        risk_list.append(make_risk_dict(risk))
    return json.dumps(risk_list, indent=2)

def make_risk_dict(risk):
    """Makes a JSON serialisable dictionary out of a risk type. 
    Includes risk's child elements like fields and their field types."""
    risk_dict = {
        'ID': risk.id,
        'riskTypeName': risk.riskTypeName,
        'fields': []
    }
    for field in risk.fields:
        risk_dict['fields'].append(
            {
                'ID': field.id,
                'fieldName': field.fieldName,
                'fieldType': orm.FieldType.get(field.fieldTypeID).fieldTypeName
            }
        )
    return risk_dict
