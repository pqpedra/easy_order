const API_URL = "http://127.0.0.1:8000";

async function fetchTables() {
    try {
        const response = await fetch(`${API_URL}/tables`);
        const tables = await response.json();  // recebe a lista de mesas
        console.log(tables);  // mostra no console do navegador
        displayTables(tables); // opcional: mostra na tela
    } catch (error) {
        console.error("Error fetching tables:", error);
    }
}

// função para renderizar as mesas na página
function displayTables(tables) {
    const tablesSection = document.getElementById("tables-section");
    tablesSection.innerHTML = "<h2>Tables</h2>";
    tables.forEach(table => {
        tablesSection.innerHTML += `<p>Table ${table.number}: ${table.status}</p>`;
    });
}

// chama a função
fetchTables();