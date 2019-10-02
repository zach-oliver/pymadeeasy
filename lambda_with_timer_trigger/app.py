import sys
sys.path.insert(0, './pymadeeasy')
from chalice import Chalice, Rate
from operating_system_functions import get_current_date_time_url_str

app = Chalice(app_name="lambda_with_timer_trigger_%s" % (get_current_date_time_url_str()))
app.debug = True

# Automatically runs every 5 minutes
@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    return {"hello": "world"}
