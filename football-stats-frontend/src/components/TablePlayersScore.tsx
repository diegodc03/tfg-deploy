import * as React from 'react';
import { alpha } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import TableSortLabel from '@mui/material/TableSortLabel';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import DeleteIcon from '@mui/icons-material/Delete';
import FilterListIcon from '@mui/icons-material/FilterList';
import { visuallyHidden } from '@mui/utils';

// Models
import { ScoreAPI } from '../model/ScoreAPI';
import { useEffect } from 'react';






function getNestedValue(obj: any, path: string): any {
    return path.split('.').reduce((acc, part) => acc && acc[part], obj);
}


function descendingComparator<T>(a: T, b: T, orderBy: string): number {
    const aValue = getNestedValue(a, orderBy);
    const bValue = getNestedValue(b, orderBy);
  
    if (bValue < aValue) {
      return -1;
    }
    if (bValue > aValue) {
      return 1;
    }
    return 0;
  }

type Order = 'asc' | 'desc';

function getComparator(
    order: Order,
    orderBy: keyof ScoreAPI,
    ): (
        a: ScoreAPI,
        b: ScoreAPI,
    ) => number {
        return order === 'desc'
        ? (a, b) => descendingComparator(a, b, orderBy as string)
        : (a, b) => -descendingComparator(a, b, orderBy as string);
}
interface HeadCell {
  disablePadding: boolean;
  id: keyof ScoreAPI;
  label: string;
  numeric: boolean;
}

const headCells: readonly HeadCell[] = [
    {
        id: 'match_player_score_id',
        numeric: false,
        disablePadding: true,
        label: 'ID',
    },
    {
        id: 'match_player_id',
        numeric: false,
        disablePadding: false,
        label: 'Nombre Jugador',
    },
    {
        id: 'specific_position_id',
        numeric: false,
        disablePadding: false,
        label: 'Posicion Especifica',
    },
    {
        id: 'basic_position_id',
        numeric: false,
        disablePadding: false,
        label: 'Posición Basica',
    },
    {
        id: 'score',
        numeric: true,
        disablePadding: false,
        label: 'Puntuación',
    },
    {
        id: 'game_mode_id',
        numeric: false,
        disablePadding: false,
        label: 'Forma de Juego',
    },
];

interface EnhancedTableProps {
    numSelected: number;
    onRequestSort: (event: React.MouseEvent<unknown>, property: keyof ScoreAPI) => void;
    order: Order;
    orderBy: string;
    rowCount: number;
}

function EnhancedTableHead(props: EnhancedTableProps) {
    
    const { order, orderBy, numSelected, rowCount, onRequestSort } =
        props;
    const createSortHandler =
        (property: keyof ScoreAPI) => (event: React.MouseEvent<unknown>) => {
        onRequestSort(event, property);
        };



    return (
        <TableHead>
        <TableRow>
            <TableCell padding="checkbox">
            
            </TableCell>
            {headCells.map((headCell) => (
            <TableCell
                key={headCell.id}
                align={headCell.numeric ? 'right' : 'left'}
                padding={headCell.disablePadding ? 'none' : 'normal'}
                sortDirection={orderBy === headCell.id ? order : false}
            >
                <TableSortLabel
                active={orderBy === headCell.id}
                direction={orderBy === headCell.id ? order : 'asc'}
                onClick={createSortHandler(headCell.id)}
                >
                {headCell.label}
                {orderBy === headCell.id ? (
                    <Box component="span" sx={visuallyHidden}>
                    {order === 'desc' ? 'sorted descending' : 'sorted ascending'}
                    </Box>
                ) : null}
                </TableSortLabel>
            </TableCell>
            ))}
        </TableRow>
        </TableHead>
    );
}



export default function EnhancedTable({rows}: {rows: ScoreAPI[]}) {


    const [order, setOrder] = React.useState<Order>('asc');
    const [orderBy, setOrderBy] = React.useState<keyof ScoreAPI>('match_player_score_id');
    const [selected, setSelected] = React.useState<readonly number[]>([]);
    const [page, setPage] = React.useState(0);
    const [dense, setDense] = React.useState(true);
    const [rowsPerPage, setRowsPerPage] = React.useState(10);


    useEffect(() => {
       console.log("Rows updated"); // Log the updated rows
    }
    , [rows]); // Add rows as a dependency


    const handleRequestSort = (
        event: React.MouseEvent<unknown>,
        property: keyof ScoreAPI,
    ) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
    };


    const handleClick = (event: React.MouseEvent<unknown>, id: number) => {
        const selectedIndex = selected.indexOf(id);
        let newSelected: readonly number[] = [];

        if (selectedIndex === -1) {
        newSelected = newSelected.concat(selected, id);
        } else if (selectedIndex === 0) {
        newSelected = newSelected.concat(selected.slice(1));
        } else if (selectedIndex === selected.length - 1) {
        newSelected = newSelected.concat(selected.slice(0, -1));
        } else if (selectedIndex > 0) {
        newSelected = newSelected.concat(
            selected.slice(0, selectedIndex),
            selected.slice(selectedIndex + 1),
        );
        }
        setSelected(newSelected);
    };

    const handleChangePage = (event: unknown, newPage: number) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };

    const handleChangeDense = (event: React.ChangeEvent<HTMLInputElement>) => {
        setDense(event.target.checked);
    };

    const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;

    const visibleRows = React.useMemo(
        () =>
        [...rows]
            .sort(getComparator(order, orderBy))
            .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage),
        [rows, order, orderBy, page, rowsPerPage],
    );

    return (
        <Box sx={{ width: '100%' }}>
        <Paper sx={{ width: '100%', mb: 2 }}>
        <Toolbar
            sx={[
                {
                pl: { sm: 2 },
                pr: { xs: 1, sm: 1 },
                }
            ]}
            >
            <Typography
                sx={{ flex: '1 1 100%' }}
                variant="h6"
                id="tableTitle"
                component="div"
                >
                Puntuaciones
            </Typography>
        </Toolbar>
            <TableContainer>
                <Table
                    sx={{ minWidth: 750 }}
                    aria-labelledby="tableTitle"
                    size={dense ? 'small' : 'medium'}
                >
                    {
                    <EnhancedTableHead
                    numSelected={selected.length}
                    order={order}
                    orderBy={orderBy}

                    onRequestSort={handleRequestSort}
                    rowCount={rows.length}
                    />
                    }
                    <TableBody>
                    {
                        visibleRows.map((row, index) => {
                        const labelId = `enhanced-table-checkbox-${index}`;

                        return (
                        <TableRow
                            hover
                            onClick={(event) => handleClick(event, row.match_player_score_id)}
                            role="checkbox"
                            tabIndex={-1}
                            key={row.match_player_score_id}
                            sx={{ cursor: 'pointer' }}
                        >
                            <TableCell padding="checkbox">
                            </TableCell>
                            <TableCell 
                                padding="none">{row.match_player_score_id}
                            </TableCell> {/* ID visible */}
                            <TableCell
                                component="th"
                                id={labelId}
                                scope="row"
                                padding="none"
                                >
                                {row.match_player_id?.player_id?.player_name ?? 'N/A'}
                            </TableCell>
                            <TableCell align="right">
                                {row.specific_position_id?.specific_position_name === "no_existencia"
                                ? 'Puntuacion Basica'
                                : row.specific_position_id?.specific_position_name ?? 'N/A'
                                }
                            </TableCell>
                            <TableCell align="right">{row.basic_position_id?.category_name ?? 'N/A'}</TableCell>
                            <TableCell align="right">{row.score}</TableCell>
                            <TableCell align="right">
                                {row.game_mode_id?.game_mode_name === "no_existencia"
                                ? 'Puntuacion Basica'
                                : row.game_mode_id?.game_mode_name ?? 'N/A'
                                }
                            </TableCell>
                        </TableRow>
                        );
                    })}
                    {emptyRows > 0 && (
                        <TableRow
                        style={{
                            height: (dense ? 33 : 53) * emptyRows,
                        }}
                        >
                        <TableCell colSpan={6} />
                        </TableRow>
                    )}
                    </TableBody>
                </Table>
            </TableContainer>
            <TablePagination
                rowsPerPageOptions={[5, 10, 25]}
                component="div"
                count={rows.length}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
            />
        </Paper>
        <FormControlLabel
            control={<Switch checked={dense} onChange={handleChangeDense} />}
            label="Dense padding"
        />
        </Box>
    );
}
