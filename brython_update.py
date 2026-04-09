

from browser import ajax, timer, document

window.addEventListener("sandbox_signal", e => {

    const signal = e.detail;

    quantumNodes.forEach(q=>{
        if(signal.level === "quantum"){
            q.material.color.setHex(0x00ffff);
            setTimeout(()=>{
                q.material.color.setHex(0xff00ff);
            },300);
        }
    });
});




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