EQ_model = BayesianNetwork(
    [
        ("Burglary", "Alarm"),
        ("Earthquake", "Alarm"),
        ("Alarm", "JohnCalls"),
        ("Alarm", "MaryCalls"),
    ]
)
cpd_B = TabularCPD(variable="Burglary", variable_card=2, values=[[0.001], [1 - 0.001]])

cpd_E = TabularCPD(variable="Earthquake", variable_card=2, values=[[0.002], [1 - 0.002]])

cpd_A = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[[0.95, 0.94, 0.29, 0.001], [1 - 0.95, 1 - 0.94, 1 - 0.29, 1 - 0.001]],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
)

cpd_J = TabularCPD(
    variable="JohnCalls",
    variable_card=2,
    values=[[0.90, 0.05], [0.10, 0.95]],
    evidence=["Alarm"],
    evidence_card=[2],
)

cpd_M = TabularCPD(
    variable="MaryCalls",
    variable_card=2,
    values=[[0.70, 0.01], [0.30,0.99]],
    evidence=["Alarm"],
    evidence_card=[2],
)
# Associating the parameters with the model structure.
EQ_model.add_cpds(cpd_B, cpd_E, cpd_A, cpd_J, cpd_M)

# Checking if the cpds are valid for the model.
EQ_model.check_model()

print(EQ_model.get_cpds("Burglary"))
print(EQ_model.get_cpds("Earthquake"))
print(EQ_model.get_cpds("Alarm"))
print(EQ_model.get_cpds("JohnCalls"))
print(EQ_model.get_cpds("MaryCalls"))
print("Nodes in the model:", EQ_model.nodes())

# Check for d-separation between variables
print(EQ_model.is_dconnected("Burglary", "Earthquake"))
print(EQ_model.is_dconnected("Burglary", "Earthquake", observed=["Alarm"]))

EQ_infer = VariableElimination(EQ_model)
# Query 1
q = EQ_infer.query(variables=["MaryCalls"], evidence={"Alarm":0})
print(q)
output = "Yes " if q.values[0] > q.values[1] else "No"
print('\n' +output)

# Query 2
print("Probability of burglary given both of them call\n")
q = EQ_infer.query(variables=["Burglary"], evidence={"MaryCalls":0,"JohnCalls":0})
print(q)
output = "Yes " if q.values[0] > q.values[1] else "No"
print('\n' +output)

# Query 3
print("Probability of Alarm given both of them call\n")
q = EQ_infer.query(variables=["Alarm"], evidence={"MaryCalls":0,"JohnCalls":0})
print(q)
output = "Yes " if q.values[0] > q.values[1] else "No"
print('\n' +output)
