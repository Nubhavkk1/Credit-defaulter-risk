async function predict() {

    const data = {
        utilisation: parseFloat(document.getElementById("util").value),
        avg_payment_ratio: parseFloat(document.getElementById("avg_pay").value),
        min_due_paid_freq: parseFloat(document.getElementById("min_due").value),
        merchant_mix: parseFloat(document.getElementById("mix").value),
        cash_withdrawal: parseFloat(document.getElementById("cash").value),
        recent_spend_change: parseFloat(document.getElementById("spend").value)
    };

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();
    const probability = result.default_probability * 100;

    const output = document.getElementById("output");
    output.classList.remove("hide");

    if (probability < 33) output.className = "result low";
    else if (probability < 66) output.className = "result medium";
    else output.className = "result high";

    output.innerHTML = "Default Probability: " + probability.toFixed(2) + "%";
}



async function predictCSV() {
    const fileInput = document.getElementById("csvFile");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload a CSV file!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/predict_csv", {
        method: "POST",
        body: formData
    });

    const results = await response.json();

    const table = document.getElementById("csvTable");
    const tbody = document.getElementById("csvTableBody");
    table.classList.remove("hide");
    tbody.innerHTML = "";

    results.forEach((prob, index) => {
        let riskClass = prob < 0.33 ? "low" : prob < 0.66 ? "medium" : "high";
        let riskLevel = prob < 0.33 ? "Low" : prob < 0.66 ? "Medium" : "High";

        let row = `
            <tr>
                <td>${index + 1}</td>
                <td>${(prob * 100).toFixed(2)}%</td>
                <td class="${riskClass}">${riskLevel}</td>
            </tr>
        `;

        tbody.innerHTML += row;
    });
}
