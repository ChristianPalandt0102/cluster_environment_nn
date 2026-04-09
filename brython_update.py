from browser import ajax, timer, document

def update_score():

    req = ajax.ajax()
    req.open("GET","/consciousness",True)

    def complete(ev):
        data = req.json
        document["consciousnessMeter"].text = \
            f"Consciousness: {round(data['score'],2)}"

    req.bind("complete",complete)
    req.send()

timer.set_interval(update_score,2000)