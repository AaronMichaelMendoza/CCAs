# OODA

## About

This project simulates a simplified AI system based on the OODA loop: Observe, Orient, Decide, Act. It models a combat drone making decisions in real time when confronted by enemies.

The simulation is written in Python using Pygame and emphasizes:

- Autonomous agent decision-making
- Threat scoring
- Tactical response
- Realistic movement and constraint logic

## Setup
Create a Conda environment with Python 3.10.
```bash
conda create -n ooda_sim python=3.10
conda activate ooda_sim
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the sim:
```bash
python main.py
```

## The OODA Cycle
The agent (a “friend” drone) executes the following loop every frame:

| Stage      | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| **Observe** | Scans the environment and gathers distances to all enemy drones            |
| **Orient**  | Calculates a threat score for each enemy based on proximity                |
| **Decide**  | Selects a tactic: flee from the most threatening enemy or idle             |
| **Act**     | Applies directional movement or passive bounce logic                       | 

All stages are modularized in code to reflect real-world autonomy system architecture.

## Features
- Multi-agent 2D simulation with basic physics
- OODA-based AI control structure
- Threat scoring using inverse-distance logic
- Flee vs. idle tactical decision-making
- Boundary enforcement and escape behavior
- Easily extendable architecture for advanced tactics or imperfect sensing

## Roadmap
Planned enhancements:
- Add threat scoring based on angle and velocity
- Simulate sensor noise and imperfect information
- Add multi-drone coordination
- Improve visual fidelity (drone models, threat indicators, etc)