import styles from "./TyreTable.module.css";

export default function TyreTable({
	tyres,
	onSort,
	sortConfig = { key: null, direction: null },
}) {
	if (!tyres || tyres.length === 0) {
		return (
			<div className={styles.empty}>
				No tyres match your filters. Start by entering a tyre size.
			</div>
		);
	}

	const headers = [
		{ key: "brand", label: "Brand" },
		{ key: "model", label: "Model" },
		{ key: "size", label: "Size" },
		{ key: "load_rate", label: "Load Rate" },
		{ key: "speed_rate", label: "Speed Rate" },
		{ key: "season", label: "Season" },
		{ key: "supplier", label: "Supplier" },
		{ key: "fuel_efficiency", label: "Fuel Efficiency" },
		{ key: "noise_level", label: "Noise Level (dB)" },
		{ key: "weather_efficiency", label: "Weather Efficiency" },
		{ key: "ev_approved", label: "EV Approved" },
		{ key: "cost", label: "Cost (€)" },
		{ key: "retail_cost", label: "Retail Cost (€)" },
		{ key: "quantity", label: "Quantity" },
	];

	function renderArrow(column) {
		if (!sortConfig.key || sortConfig.key !== column) return "↕";
		return sortConfig.direction === "asc" ? "↑" : "↓";
	}

	return (
		<div className={styles.tableWrapper}>
			<table className={styles.table}>
				<thead>
					<tr className={styles.headRow}>
						{headers.map((h) => (
							<th
								key={h.key}
								className={styles.headCell}
								onClick={() => onSort(h.key)}
							>
								<span>{h.label}</span>
								<span className={styles.arrow}>{renderArrow(h.key)}</span>
							</th>
						))}
					</tr>
				</thead>
				<tbody>
					{tyres.map((t) => (
						<tr key={t.id} className={styles.bodyRow}>
							<td className={styles.bodyCell}>{t.brand}</td>
							<td className={styles.bodyCell}>{t.model}</td>
							<td className={styles.bodyCell}>{t.size}</td>
							<td className={styles.bodyCell}>{t.load_rate}</td>
							<td className={styles.bodyCell}>{t.speed_rate}</td>
							<td className={styles.bodyCell}>{t.season}</td>
							<td className={styles.bodyCell}>{t.supplier}</td>
							<td className={styles.bodyCell}>{t.fuel_efficiency}</td>
							<td className={styles.bodyCell}>{t.noise_level}</td>
							<td className={styles.bodyCell}>{t.weather_efficiency}</td>
							<td className={styles.bodyCell}>{t.ev_approved ? "Yes" : "No"}</td>
							<td className={styles.bodyCell}>€{t.cost}</td>
							<td className={styles.bodyCell}>€{t.retail_cost}</td>
							<td className={`${styles.bodyCell} ${t.quantity <= 4 ? styles.lowStock : ""}`}>{t.quantity}</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
}
