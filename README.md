# RouteExplorer

![Project Completion](https://img.shields.io/badge/Project%20Completion-70%25-brightgreen)

## Table of Contents
- [Introduction](#Introduction)
- [Project Overview](#Project-overview)
- [How to Install](#How-to-install)
- [How to Use](#How-to-use)
- [Contributing](#Contributing)

## Introduction

I was inspired by a captivating video that showcased the application of the A* (A Star) pathfinding algorithm visualized on the city streets of Chicago and Rome using Blender. While the video was visually appealing, I wanted to implement a similar concept without relying on Blender, making it more accessible for everyone to use and understand.

## Project Overview

RouteExplorer is a Python-based project that provides an intuitive and visually appealing way to explore city road networks and find the best routes using the A* pathfinding algorithm. It visualizes the road network with roads in orange and the A* path in green on a map of the selected city. 

[Watch the Mentioned Video](https://www.youtube.com/watch?v=CgW0HPHqFE8)

## How I Did It

I achieved this by using Python, OSMnx for fetching road network data from OpenStreetMap, Matplotlib for map visualization, and Tkinter for a clickable GUI. Here's how it works:
- You select a starting point by clicking on any road on the map.
- Next, click on the road where you want the endpoint to be.
- The A* pathfinding algorithm calculates the best route and visualizes it in real-time, highlighting the chosen path in green.

## How to Install

To use RouteExplorer, follow these steps:

1. Download the project as a ZIP file or clone the repository:
   git clone https://github.com/Xeo-V/RouteExplorer.git
2. Navigate to the project directory:
   cd RouteExplorer
3. Install the required dependencies:
   pip install osmnx matplotlib
4. Run the application:
   python route_explorer.py


## How to Use

1. Upon running the application, you will be presented with a map of the city.

2. Click on any road to select your starting point.

3. Click on another road to set your destination.

4. The A* pathfinding algorithm will calculate and visualize the best route on the map, with the chosen path displayed in green.

## Contributing

Feel free to fork this project and use it for your purposes or contribute to its development. If you have any suggestions, improvements, or bug fixes, please create a pull request or open an issue. Together, we can make RouteExplorer even better!

[GitHub Repository](https://github.com/Xeo-V/RouteExplorer)

   
