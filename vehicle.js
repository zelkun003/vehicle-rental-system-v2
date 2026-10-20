
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(question) {
    return new Promise((resolve) => {
        rl.question(question, resolve);
    });
}

async function vehicleRental() {
    console.log("=== VEHICLE RENTAL SYSTEM ===");

    try {
        const customerName = (
            await askQuestion("Enter customer name: ")
        ).trim();

        const vehicleType = (
            await askQuestion("Enter vehicle type: ")
        ).trim();

        const daysInput = await askQuestion(
            "Enter number of rental days: "
        );

        const rateInput = await askQuestion(
            "Enter daily rental rate: "
        );

        const rentalDays = Number(daysInput);
        const dailyRate = Number(rateInput);

        if (!customerName || !vehicleType) {
            console.log("Error: Name and vehicle are required.");
            return;
        }

        if (
            !daysInput.trim() ||
            !rateInput.trim() ||
            !Number.isInteger(rentalDays) ||
            rentalDays <= 0 ||
            !Number.isFinite(dailyRate) ||
            dailyRate < 0
        ) {
            console.log("Error: Enter valid rental days and rate.");
            return;
        }

        const totalCost = rentalDays * dailyRate;

        console.log("\n=== RENTAL SUMMARY ===");
        console.log("Customer:", customerName);
        console.log("Vehicle Type:", vehicleType);
        console.log("Rental Days:", rentalDays);
        console.log("Daily Rate: ₱" + dailyRate.toFixed(2));
        console.log("Total Cost: ₱" + totalCost.toFixed(2));

    } finally {
        rl.close();
    }
}

vehicleRental();
