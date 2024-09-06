export interface SortingResult {
    name: string;
    massive: number;
    time: number;
}

export interface MainWindowProps {
    sortingResults: SortingResult[];
    loading: boolean;
    sortPercent: string;
    setSortPercent: React.Dispatch<React.SetStateAction<string>>;
    fetchSortingResults: () => void;
}
