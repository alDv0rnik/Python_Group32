import json
import datetime
from typing import Any

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}


class DateFormatEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime.datetime):
            # return o.strftime('%d/%m/%y %H:%M:%S')
            return {
                "value": o.strftime('%d/%m/%y %H:%M:%S'),
                "datetime": True
            }
        elif isinstance(o, datetime.date):
            return {
                "value": o.strftime('%d/%m/%y'),
                "date": True
            }
        return json.JSONEncoder.default(self, o)


json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

with open("output.json", "w") as file:
    json.dump(data, file, cls=DateFormatEncoder)