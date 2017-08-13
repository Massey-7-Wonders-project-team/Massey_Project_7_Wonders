import React from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import {GridList, GridTitle} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import FlatButton from 'material-ui/FlatButton';
import cards from '../Components';
const styles = {
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  gridList: {
    display: 'flex',
    flexWrap: 'nowrap',
    overflowX: 'auto',
  },
  titleStyle: {
    color: 'rgb(0, 188, 212)',
  },
};
export class GameScreen extends React.Component {
    componentDidMount() {
        const token = localStorage.getItem('token');
        fetch(`/api/game/status?game_id=${this.props.gameId}`, {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                Authorization: token,
            }
        })
        .then(response => response.json())
        .then((body) => {
            // do something
            console.log(body);
            if (body.game_id) {
                this.setState({
                    game: true,
                    error: false,
                });
            } else {
                this.setState({
                    game: false,
                    error: true,
                });
            }
          var user_Cards = body.userId.cards; //gets infromation needed for hand of cards
          var userId = body.userId;
          var gameId = body.gameId;
        })
        .catch((err) => {
            // catch error
            console.log(err);
            this.setState({
                game: false,
                error: true,
            });
          });
        }

    selectedCard(card){
      var selected_card=card;
    }; //gets selected card
    playcard(card){
      this.game.checkMove(card,userId);
      this.game.playCard(card,userId);
    }; //plays card to users wonderbard
    discard(card){
      this.game.discardCard(card,user);
    }; //discard card for 3 coins
    const cardsData=[           //list of cards and names for Hand
      {img:'/cards/'+user_Cards[0].name+'.png',
      title:user_Cards[0].name,
      author:user_Cards[0]},
      {img:'/cards/'+user_Cards[1].name+'.png'
      title:user_Cards[1].name,
      author:user_Cards[1]},
      {img:'/cards/'+user_Cards[2].name+'.png',
      title:user_Cards[2].name,
      author:user_Cards[2]},
      {img:'/cards/'+user_Cards[3].name+'.png',
      title:user_Cards[3].name,
      author:user_Cards[3]}.
      {img:'/cards/'+user_Cards[4].name+'.png',
      title:user_Cards[4].name,
      author:user_Cards[4]},
      {img:'/cards/'+user_Cards[5].name+'.png',
      title:user_Cards[5].name,
      author:user_Cards[5]},
      {img:'/cards/'+user_Cards[6].name+'.png',
      title:user_Cards[6].name,
      author:user_Cards[6]},
    ];
    render() {

        return (
          const gridList = () =>(
            <div style={styles.root}>
              <GridList style={styles.gridList} cols={2.2}>
                {cardsData.map((tile) => (
                  <GridTile
                    key={tile.img}
                    title={tile.title}
                    <RadioButton
                    value='simple'
                    label='Select'
                    onChange(selectedCard(tile.author))
                    />
                    titleStyle={styles.titleStyle}
                    titleBackground="linear-gradient(to top, rgba(0,0,0,0.7) 0%,rgba(0,0,0,0.3) 70%,rgba(0,0,0,0) 100%)"
                  >
                    <img src={tile.img} />
                  </GridTile>
                ))}
              </GridList>
            </div>
          );
          const Card_selected = () => ( ///With Avatar to be added later
          <Card>
            <CardHeader
              ///title="Avatar"
              ///avatar="images/jsa-128.jpg"
            />
            <CardMedia
              overlay={<CardTitle title=selected_card.name/>}
            >
              <img src='/cards/'+selected_card.name+'.png'/>
            </CardMedia>
            <CardText>
            "Discription of what card does"
            </CardText>
            <CardActions>
              <FlatButton label="Play Card"
               onClick={playcard(selected_card)}/>
              <FlatButton label="Discard +$"
               onClick={discard(selected_card)}/>
            </CardActions>
          </Card>
        );
      );
    }
}

export default GameScreen;
