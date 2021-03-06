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

    for (let i = 0; i < unsorted.length; ++i) {
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
                        sorted.map((color, k) => {
                            return (
                                <div key={k} style={{ float: 'left', margin: 20 }}>
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
                                                      padding: 0
                                                  }}
                                                  key={index}
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
              </div>
            }
      </div>
    )
}

CardHist.propTypes = {
    history: PropTypes.array.isRequired,
};

export default CardHist;
