import React, { useState, useEffect } from 'react';

const PacketViewer = () => {
	const [packets, setPackets] = useState([]);
	const [error, setError] = useState(null);

	useEffect(() => {
		const fetchPackets = () => {
			fetch('http://127.0.0.1:5000/api/packets')
				.then(response => {
					if (!response.ok) {
						throw new Error('Network response was not ok');
					}
					return response.json();
				})
				.then(data => setPackets(data))
				.catch(error => {
					console.error('Error fetching data: ', error);
					setError(error.message);
				});
		};

		// Poll for new packets every 5 seconds
		const intervalId = setInterval(fetchPackets, 5000);

		// Clean up interval on unmount
		return () => clearInterval(intervalId);
	}, []);

	if (error) {
		return <div>Error: {error}</div>;
	}

	return (
		<div>
			<h1>Network Packets</h1>
			<table>
				<thead>
					<tr>
						<th>Ethernet Source</th>
						<th>Ethernet Destination</th>
						<th>IP Source</th>
						<th>IP Destination</th>
						<th>Protocol</th>
						<th>Length</th>
						<th>Info</th>
					</tr>
				</thead>
				<tbody>
					{packets.map((packet, index) => (
						<tr key={index}>
							<td>{packet.ethernet?.source}</td>
							<td>{packet.ethernet?.destination}</td>
							<td>{packet.ip?.source}</td>
							<td>{packet.ip?.destination}</td>
							<td>{packet.ip?.proto}</td>
							<td>{packet.ip?.length}</td>
							<td>Additional Info</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
};

export default PacketViewer;
