"use client";

import { useState, useMemo, useEffect } from "react";
import styles from "./TyreFilters.module.css";

export default function TyreFilters({ tyres, onFilter }) {
	const [size, setSize] = useState("");
	const [brand, setBrand] = useState("all");
	const [season, setSeason] = useState("all");
	const [evOnly, setEvOnly] = useState(false);

	// Create filter object once and push it to parent when any filter changes
	useEffect(() => {
		onFilter({
			size,
			brand,
			season,
			evOnly,
		});
	}, [size, brand, season, evOnly]);

	const brandOptions = useMemo(() => {
		const unique = [...new Set(tyres.map((t) => t.brand))];
		return unique.sort();
	}, [tyres]);

	return (
		<div className={styles.card}>
			<h2 className={styles.title}>Filters</h2>

			{/* Tyre Size */}
			<div className={styles.field}>
				<label className={styles.label}>Tyre Size</label>
				<input
					className={styles.input}
					placeholder="e.g. 205/55R16"
					value={size}
					onChange={(e) => setSize(e.target.value)}
				/>
			</div>

			{/* Brand */}
			<div className={styles.field}>
				<label className={styles.label}>Brand</label>
				<select
					className={styles.select}
					value={brand}
					onChange={(e) => setBrand(e.target.value)}
				>
					<option value="all">All Brands</option>
					{brandOptions.map((b) => (
						<option key={b} value={b}>
							{b}
						</option>
					))}
				</select>
			</div>

			{/* Season */}
			<div className={styles.field}>
				<label className={styles.label}>Season</label>
				<select
					className={styles.select}
					value={season}
					onChange={(e) => setSeason(e.target.value)}
				>
					<option value="all">All</option>
					<option value="Summer">Summer</option>
					<option value="Winter">Winter</option>
					<option value="All Season">All Season</option>
				</select>
			</div>

			{/* EV Approved */}
			<div className={styles.checkboxRow}>
				<input
					type="checkbox"
					checked={evOnly}
					onChange={(e) => setEvOnly(e.target.checked)}
				/>
				<label className={styles.label}>EV Approved Only</label>
			</div>
		</div>
	);
}
