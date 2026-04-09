@app.route("/gpu_score")
def gpu_score():
    return {
        "score": gpu_mind.score()
    }