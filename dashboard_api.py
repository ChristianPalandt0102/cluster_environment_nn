
@app.route("/consciousness")
def consciousness():
    return {"score": meter.score()}

@app.route("/gpu_score")
def gpu_score():
    return {
        "score": gpu_mind.score()
    }