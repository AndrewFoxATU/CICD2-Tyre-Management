import Image from "next/image";
import TyresClient from "./tyres-client";
import { fetchTyres } from "../../../lib/api";
import styles from "./TyresPage.module.css";

export default async function TyresPage() {
	const tyres = await fetchTyres();

	return (
		<main className={styles.page}>
			<div className={styles.box}>
				<header className={styles.header}>
                    <Image
                        src="/logo.avif"
                        alt="Ballinasloe Tyres"
                        width={800}
                        height={200}
                        className={styles.logo}
                    />
				</header>

				<TyresClient initialTyres={tyres} />
			</div>
		</main>
	);
}
