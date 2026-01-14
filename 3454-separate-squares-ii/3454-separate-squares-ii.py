class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # 1. Coordinate Compression for X-axis
        # We need all unique x and x+l points to build the leaves of our segment tree
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        
        # Sort distinct x coordinates and map them to indices
        xs = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(xs)}
        n_map = len(xs)
        
        # 2. Build Events for Sweep Line on Y-axis
        # (y_coord, type, x_start_idx, x_end_idx)
        # type: +1 for bottom edge (add square), -1 for top edge (remove square)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x_map[x], x_map[x + l]))
            events.append((y + l, -1, x_map[x], x_map[x + l]))
            
        events.sort() # Sort by Y coordinate
        
        # 3. Segment Tree Setup
        # count: how many squares currently cover this segment
        # length: the total length of the union of squares in this segment
        count = [0] * (4 * n_map)
        length = [0.0] * (4 * n_map)
        
        def update(node, start, end, l, r, val):
            if r <= xs[start] or l >= xs[end]:
                return
            
            if l <= xs[start] and xs[end] <= r:
                count[node] += val
            else:
                mid = (start + end) // 2
                update(2 * node, start, mid, l, r, val)
                update(2 * node + 1, mid, end, l, r, val)
            
            # Update 'length' for the current node
            if count[node] > 0:
                # If this node is covered by at least one square, its length is the full width
                length[node] = xs[end] - xs[start]
            else:
                # If leaf node, length is 0 (since count is 0)
                # If internal node, length is sum of children
                if end - start == 1:
                    length[node] = 0.0
                else:
                    length[node] = length[2 * node] + length[2 * node + 1]

        # 4. Calculate Total Area first
        # We need the total area to know when to stop
        # Note: We can actually do this in one pass, but calculating total first is cleaner logic
        # Re-using the same sweep-line logic is tricky if we want to stop halfway.
        # A simpler way: Run the sweep line fully to get Total Area. 
        # Then reset and run again to find the cut.
        
        # Let's perform a full sweep to record the area at every Y step.
        total_area = 0.0
        prev_y = events[0][0]
        
        # Determine total area and keep track of accumulated area at each step
        # To avoid running sweep twice, we store the "area segments"
        # (y_bottom, y_top, width_during_this_segment)
        segments = [] 
        
        for y, typ, x_start, x_end in events:
            width = length[1] # Root of segment tree holds total active width
            height = y - prev_y
            
            if height > 0:
                seg_area = width * height
                total_area += seg_area
                segments.append((prev_y, y, width, seg_area))
                
            # Update tree for the current event
            # Note: we pass xs[x_end] as the right boundary coordinate value
            update(1, 0, n_map - 1, xs[x_start], xs[x_end], typ)
            prev_y = y
            
        # 5. Find the Split Line
        target = total_area / 2.0
        current_area = 0.0
        
        for y1, y2, width, seg_area in segments:
            if current_area + seg_area >= target:
                # The target line is inside this horizontal strip
                needed = target - current_area
                # width * (ans - y1) = needed
                # ans - y1 = needed / width
                if width == 0: return y1 # Should not happen if area > 0
                return y1 + (needed / width)
            current_area += seg_area
            
        return prev_y