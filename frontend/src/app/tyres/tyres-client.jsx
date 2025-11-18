"use client";

import { useState } from "react";
import TyreFilters from "../../../components/TyreFilters";
import TyreTable from "../../../components/TyreTable";
import styles from "./TyresClient.module.css";

export default function TyresClient({ initialTyres }) {
	const [filtered, setFiltered] = useState([]);
	const [sortConfig, setSortConfig] = useState({
		key: null,
		direction: null,
	});

	function applyFilters(filters) {
        const { size, brand, season, evOnly } = filters;

        // Start with ALL tyres
        let list = [...initialTyres];

        // Tyre size filter (only if typed)
        if (size && size.trim() !== "") {
            list = list.filter((t) =>
                t.size.toLowerCase().includes(size.toLowerCase())
            );
        }

        // Brand filter
        if (brand && brand !== "all") {
            list = list.filter((t) => t.brand === brand);
        }

        // Season filter
        if (season && season !== "all") {
            list = list.filter((t) => t.season === season);
        }

        // EV approved filter
        if (evOnly) {
            list = list.filter((t) => t.ev_approved === true);
        }

        // Default sorting: most in stock first
        list.sort((a, b) => b.quantity - a.quantity);

        setFiltered(list);
        setSortConfig({
            key: "quantity",
            direction: "desc",
        });
    }


	function handleSort(column) {
		if (!filtered || filtered.length === 0) return;

		const sampleValue = filtered[0][column];
		const isNumber = typeof sampleValue === "number";

		let direction;

		if (sortConfig.key === column) {
			direction = sortConfig.direction === "asc" ? "desc" : "asc";
		} else {
			direction = isNumber ? "desc" : "asc";
		}

		setSortConfig({ key: column, direction });

		const sorted = [...filtered].sort((a, b) => {
			const A = a[column];
			const B = b[column];

			if (isNumber) {
				return direction === "asc" ? A - B : B - A;
			}

			return direction === "asc"
				? String(A).localeCompare(String(B))
				: String(B).localeCompare(String(A));
		});

		setFiltered(sorted);
	}

	return (
		<div className={styles.layout}>
			<div className={styles.sidebar}>
				<TyreFilters tyres={initialTyres} onFilter={applyFilters} />
			</div>

			<div className={styles.tableArea}>
				<TyreTable
					tyres={filtered}
					onSort={handleSort}
					sortConfig={sortConfig}
				/>
			</div>
		</div>
	);
}
