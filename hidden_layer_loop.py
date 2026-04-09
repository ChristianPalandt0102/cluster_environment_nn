def gpu_feedback_cycle(gpu, cache, dream):
    while True:

        gpu.randomize()

        future = dream.simulate_gpu_future(gpu)

        if future["stability_index"] < 0.4:
            cache.integrate_pattern([1]*5000)

        time.sleep(2)