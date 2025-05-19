import datetime

def run_report(request):
  """
  do your computation here
  """
  return {
    "success":True,
    "timeStamp":datetime.datetime.now().isoformat()
  }, 200