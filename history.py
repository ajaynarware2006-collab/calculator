def save_history(data):
    with open("PROJECTS/calculater/history.txt","a") as f:
        f.write(f"{data}\n")
    
def read_history():
    with open("PROJECTS/calculater/history.txt","r") as f:
        content=f.read()
        return content

def clear_history():
    with open("PROJECTS/calculater/history.txt","w") as f:
        return
