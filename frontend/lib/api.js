export async function fetchTyres() {
	const res = await fetch("http://localhost:8001/api/tyres", {
		cache: "no-store",
	});

	if (!res.ok) throw new Error("Failed to fetch tyres");

	return res.json();
}
