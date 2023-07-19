import schedule
import time

def task():
    print("tache planifiée")

# Planifier la tâche pour qu'elle s'exécute toutes les 5 secondes
schedule.every(5).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    # Arrêter la tâche après 30 secondes
    #if time.time() - scheduled_task.last_run >= 30:
     #   scheduled_task.cancel()
      #  break