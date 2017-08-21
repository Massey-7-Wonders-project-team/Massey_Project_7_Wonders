function CityBoard(props) {

  return (
    <div>
		<img src={baseLocation + `../images/cities/${props.name}.png`} />
		<center><h3>City: {props.name}</h3></center>
    </div>
    );
}

function Player(props) {
   return <div>
      <center><h1>Player: {props.player} <i> (ID: {props.ID}) </i></h1></center>
      </div>;
}

function Inventory (props) {
   return(
     <tr>
       <td><img height="20" src={baseLocation + `icons/${props.item}.png`} /></td>
	   <td>{props.item}:</td>
	   <td> {props.amount}</td>
     </tr>
     );
}

function PlayerDisplay(props) {

   // hardcoded information recieved from back end...

  const recievedJSN = {
    'player': {
      'id': 1,
      'gameId': 1,
      'userId': 1,
      'name': 'Sara',
      'ready': 'False',
      'city': 'rhodosA',
      'wood': 0,
      'brick': 0,
      'ore': 0,
      'stone': 2,
      'glass': 1,
      'paper': 0,
      'cloth': 1,
      'points': 0,
      'military': 0,
      'money': 0},
    'cards': []
  };


  //var playerDetails = recievedJSN.player;
  var playerDetails = {props.data}.player;

	const divStyle = {
	backgroundColor: 'lightblue',
	padding : '0'
	};


   return (
    <div>
    <table style={divStyle}>
	  <tr>
	  <td ><p><u>Inventory</u></p>
	  <table>
         <Inventory item="wood" amount={playerDetails.wood} />
         <Inventory item="brick" amount={playerDetails.brick} />
         <Inventory item="ore" amount={playerDetails.ore} />
         <Inventory item="stone" amount={playerDetails.stone} />
         <Inventory item="glass" amount={playerDetails.glass} />
         <Inventory item="paper" amount={playerDetails.paper} />
         <Inventory item="cloth" amount={playerDetails.cloth} />
       </table>
	   </td>
	   <td>
	   <Player player={playerDetails.name} ID={playerDetails.userId} />
	   <CityBoard name={playerDetails.city} /></td>
       <td>
       <p><u>Buildings</u></p>
       <table style={divStyle}>
         <Inventory item="military" amount={playerDetails.military} />
       </table>
       <p><u>Others</u></p>
       <table style={divStyle}>
         <Inventory item="Coin" amount={playerDetails.money} />
         <Inventory item="VP" amount={playerDetails.points} />
       </table>
	   </td></tr>
	</table>
     </div>
  );
}

export default PlayerDisplay;
