## DIRECTED ACYCLIC GRAPH (DAG)
Is a conceptual representation of a series of activities. The order of the activities is depicted by a graph, which is visually presented as a set of circles, each one representing an activity, some of which are connected by lines, which represent the flow from one activity to another.
<img src="dag1.png" width=280 height=190 />
1. “Directed” means that each edge has a defined direction, so each edge necessarily represents a single directional flow from one vertex to another
2. “Acyclic” means that there are no loops (i.e., “cycles”) in the graph, so that for any given vertex, if you follow an edge that connects that vertex to another, there is no path in the graph to get back to that initial vertex
3. "Graph" is a collection of vertices (or point) and edges (or lines) that indicate connections between the vertices

## DATA ORCHESTRATION
When a person (or a team) wants to put a data asset (a table, a file, a lake) in production that's not done in a vacuum, data must come from somewhere and go somewhere  
You need a workflow manager or orchestration system to model those dependencies and ensure those computations that produce data are scheduled and orderly correctly

#### ROLES THAT ORCHESTRATION INVOLVES
1. Practitioner: Responsible for the production of data assets (data engineer / data science)
2. Stakeholders: Care about data assets and often are ops people business analysts, they care about the data consumed, a kind of self-serve on top of the platform and even do operational tasks
3. Platform: Responsible for the data infrastructure and support practitioners and stakeholders.  One of their primary jobs are to enable end-to end ownership by practitioners over their data asset production

#### The natural center of gravity between that roles is the orchestrator
(The dominant engines are Apache Airflow, Luigi, Kubeflow, MLflow, Argo, Dagster, ...)
