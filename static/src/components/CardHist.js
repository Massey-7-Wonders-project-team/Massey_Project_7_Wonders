import React, { PropTypes } from 'react';
import { CardMedia, Table, TableBody, TableRow, TableRowColumn } from 'material-ui';

function sortByColor(props) {
    const unsorted = props;

    let brown = [];
    let grey = [];
    let yellow = [];
    let blue = [];
    let green = [];
    let red = [];

    for (let i = 1; i < unsorted.length; ++i) {
        if (unsorted[i].card_colour === 'brown') { brown.push(unsorted[i]); }
        if (unsorted[i].card_colour === 'grey') { grey.push(unsorted[i]); }
        if (unsorted[i].card_colour === 'yellow') { yellow.push(unsorted[i]); }
        if (unsorted[i].card_colour === 'blue') { blue.push(unsorted[i]); }
        if (unsorted[i].card_colour === 'green') { green.push(unsorted[i]); }
        if (unsorted[i].card_colour === 'red') { red.push(unsorted[i]); }
    }

    return [brown, grey, blue, yellow, red, green];
}

function CardHist(props) {
    let cardsPlayed = props.history;
    const sorted = sortByColor(props.history);
    return (
      <div>
          {!cardsPlayed &&
              <div>
                  <h3> You have not played any cards yet... </h3>
              </div>
          }
          {cardsPlayed &&
            <div style={{ display: 'inline-block' }}>
                <p><b>All your Cards played</b></p>
                <div>
                  {sorted &&
                    sorted.map((color, cIndex) => {
                      return(
                        <div style={{ float: 'left', margin: 20 }}>
                          {color &&
                            color.map((card, index) => {
                                const imageName = (card.card_name).replace(/\s+/g, '').toLowerCase();
                                let marginLeft = -60;
                                if (index === 0) { marginLeft = 0; }
                                const topMargin = index * 32;
                                return (
                                    <CardMedia
                                        style={{
                                            marginLeft: `${marginLeft}`,
                                            width: 90,
                                            display: 'inline-block',
                                            padding: 0 }}
                                    >
                                        <img
                                            alt={`${card.card_name} image`}
                                            src={`dist/images/cards/${imageName}.png`}
                                            style={{
                                                paddingTop: topMargin,
                                                width: 90,
                                                display: 'inline-block',
                                            }}
                                        />
                                    </CardMedia>
                              );
                            })
                          }
                      </div>
                    )
                    })
                  }
              </div>
          }
      </div>
    }
    </div>
  )
}

CardHist.propTypes = {
    history: PropTypes.object.isRequired,
import { Card, CardText, CardHeader, CardMedia, CardTitle, GridList } from 'material-ui';

function CardHist(props) {
    let cardsPlayed = props.historyData;
    return (
      <div>
        <p><b>All your Cards played</b></p>
        <div>
            {cardsPlayed &&
                cardsPlayed.map((card, index) => {
                    const imageName = (card.card_name).replace(/\s+/g, '').toLowerCase();
                    let margin = -20;
                    if (index === 1) { margin = 0; }
                    if (index > 0)
                    {
                      return (
                        <Card
                            className="Card"
                            data-card-number={index}
                            key={card.id}
                            style={{
                                margin: `${margin}`,
                                width: 90, display:
                                'inline-block',
                                padding: 0 }}
                        >
                            <CardMedia>
                                <img
                                    alt={`${card.card_name} image`}
                                    src={`dist/images/cards/${imageName}.png`}
                                />
                            </CardMedia>
                        </Card>
                    );
                  }
                })
            }
      </div>
      </div>
    );
}

CardHist.propTypes = {
    historyData: PropTypes.object.isRequired,
};

export default CardHist;
